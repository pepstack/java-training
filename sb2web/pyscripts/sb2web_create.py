#!/usr/bin/python
#-*- coding: UTF-8 -*-
#
# @file: sb2web_create.py
#
# @version:
# @create:
# @update: 2019-09-20
#
#######################################################################
from __future__ import print_function
import os, sys, stat, signal, shutil, inspect, commands, time, datetime

import yaml, codecs, json, base64

import optparse, ConfigParser

# http://docs.jinkan.org/docs/jinja2/
# http://docs.jinkan.org/docs/jinja2/templates.html
from jinja2 import Environment, PackageLoader, FileSystemLoader

#######################################################################
# application specific
APPFILE = os.path.realpath(sys.argv[0])
APPHOME = os.path.dirname(APPFILE)
APPNAME,_ = os.path.splitext(os.path.basename(APPFILE))
APPVER = "1.0.0"
APPHELP = "Create java springboot2 web project."

#######################################################################
# import your local modules
import utils.utility as util
import utils.evntlog as elog

from utils.error import try_except_log

#######################################################################

@try_except_log
def validate_options_config (options):
    elog.info("validate options...")

    if not options.name:
        options.name = options.artifact.replace("-", "")

    if not options.packagename:
        options.packagename = options.group + "." + options.name

    if options.packaging.capitalize() != "Jar" and options.packaging.capitalize() != "War":
        raise Exception("packaging not Jar or War")

    options.packaging = options.packaging.capitalize()

    if options.java != "8":
        raise Exception("java version not 8")

    if not options.context_path:
        options.context_path = "/"

    if options.context_path == "$name":
        options.context_path = options.name


@try_except_log
def start_run_project (artifactDir):
    runcmd = "mvn spring-boot:run"
    elog.force(runcmd)
    os.chdir(artifactDir)
    os.system(runcmd)
    pass


########################################################################
@try_except_log
def read_file_content (pathfile):
    content = ""
    fd = util.open_file(pathfile, mode='r+b', encoding='utf-8')
    for line in fd.readlines():
        content += line.encode('utf-8')
    fd.close()
    return content


@try_except_log
def write_out_file(fout, outcontent):
    util.write_file_utf8(fout, outcontent.encode('utf-8'))
    pass


@try_except_log
def render_output_file (srcfile, dstfile, renderConfig, verbose = True):
    dstpath = os.path.dirname(dstfile)
    dstname = os.path.basename(dstfile)

    outputfile = os.path.join(dstpath, dstname)

    srcfileRelPath = os.path.relpath(srcfile, renderConfig.j2envRoot)

    j2tmpl = renderConfig.j2env.get_template(srcfileRelPath)

    outcontent = j2tmpl.render(**renderConfig)

    util.create_output_file(outputfile, write_out_file, outcontent, False)
    pass


@try_except_log
def copy_template (srcfile, dstfile, renderConfig, verbose):
    _, ext = os.path.splitext(os.path.basename(srcfile))

    if ext == ".template":
        # 需要模板处理
        dstname, _ = os.path.splitext(dstfile)
        if verbose:
            util.info2("render file: %s -> %s" % (srcfile, dstname))
        render_output_file(srcfile, dstname, renderConfig, verbose)
    else:
        # 不需要模板处理, 直接复制
        if verbose:
            util.info("copy file: %s -> %s" % (srcfile, dstfile))
        shutil.copyfile(srcfile, dstfile)
    pass


########################################################################
@try_except_log
def create_sb2web_project (appConfig, options):
    artifactDir = os.path.join(appConfig.projectsDir, options.artifact)

    elog.info("starting create project: %s", artifactDir)

    if util.dir_exists(artifactDir):
        util.warn("artifact already exists: %s" % artifactDir)
        if not options.force:
            util.warn("using '--force' to ovewrite it");
            sys.exit(0)
        pass
    
    try:
        shutil.rmtree(artifactDir)
    except:
        pass

    pairConfig = (
        util.DotDict(
            
        ),
        util.DotDict(
            
        )
    )

    # 载入模板工程的配置文件
    templateDict = {}
    templateYaml = os.path.join(appConfig.sb2webRoot, "j2template.yaml")
    if util.file_exists(templateYaml):
        fd = open(templateYaml)
        templateDict = yaml.load(fd.read())
        fd.close()


    renderConfig = util.DotDict(
        LICENSE_HEADER = read_file_content(os.path.join(APPHOME, 'license_header.txt'))
        ,j2envRoot     = appConfig.sb2webRoot
        ,j2env         = Environment(loader=FileSystemLoader(appConfig.sb2webRoot))
        ,templateDict  = templateDict
        ,springbootVer = options.springboot
        ,groupId       = options.group
        ,artifactId    = options.artifact
        ,artifactName  = options.name
        ,artifactVer   = options.ver
        ,description   = options.description
        ,packageName   = options.packagename
        ,packaging     = options.packaging
        ,javaVersion   = options.java
        ,serverPort    = options.port
        ,contextPath   = options.context_path
    )

    # 复制目录树, 同时处理模板文件
    util.copydirtree(appConfig.sb2webRoot, artifactDir, pairConfig, True, copy_template, renderConfig)

    elog.info("success create project: %s", artifactDir)

    if options.run:
        elog.info("starting run: %s", artifactDir)
        start_run_project(artifactDir)
    pass


########################################################################
# 主函数仅仅处理日志和检查配置项
#
def main(parser, appConfig):
    import utils.logger as logger
    (options, args) = parser.parse_args(args=None, values=None)
    loggerConfig = util.DotDict(
        logging_config = options.log_config
        ,file = APPNAME + '.log'
        ,name = options.logger
    )
    logger_dictConfig = logger.set_logger(loggerConfig, options.log_path, options.log_level)

    validate_options_config(options)

    util.print_options_attrs2(options, [
            ("springboot", "version"),
            ("group", "groupId"),
            ("artifact", "artifactId"),
            ("name", "name"),
            ("ver", "artifact.version"),
            ("description", "description"),
            ("packagename", "packageName"),
            ("packaging", "packaging"),
            ("java", "java.version"),
            ("port", "server.port"),
            ("context_path", "server.servlet.context-path"),
        ])

    create_sb2web_project(appConfig, options)
    pass


#######################################################################
# Usage:
#    $ %prog
#  or
#    $ %prog --force
#
if __name__ == "__main__":
    parser, group, optparse, profile = util.init_parser_group(
        apphome = APPHOME,
        appname = APPNAME,
        appver = APPVER,
        apphelp = APPHELP,
        usage = "%prog [Options]",
        group_options = os.path.join(APPHOME, "options/sb2web_options.yaml")
    )

    print(profile)

    appRoot = os.path.dirname(APPHOME)

    # 应用程序的本地缺省配置
    appConfig = util.DotDict(
        appRoot = appRoot
        ,sb2webRoot = os.path.join(APPHOME, "sb2web")
        ,projectsDir = os.path.join(appRoot, "projects")
    )

    # 主函数
    main(parser, appConfig)
    sys.exit(0)
