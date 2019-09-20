# springboot2-webapp-sample01

```
/***********************************************************************
* Copyright (c) 2018 pepstack, pepstack.com
*
* This software is provided 'as-is', without any express or implied
* warranty.  In no event will the authors be held liable for any damages
* arising from the use of this software.
* Permission is granted to anyone to use this software for any purpose,
* including commercial applications, and to alter it and redistribute it
* freely, subject to the following restrictions:
*
* 1. The origin of this software must not be misrepresented; you must not
*   claim that you wrote the original software. If you use this software
*   in a product, an acknowledgment in the product documentation would be
*   appreciated but is not required.
*
* 2. Altered source versions must be plainly marked as such, and must not be
*   misrepresented as being the original software.
*
* 3. This notice may not be removed or altered from any source distribution.
***********************************************************************/
```


参考:

	https://blog.csdn.net/ubuntu64fan/article/details/80555372


基于 maven 构建:

	$ mvn clean compile package
	
	$ mvn spring-boot:run
	或
	$ java -jar ./target/webapp-0.0.1-SNAPSHOT.jar


浏览器访问:

	http://localhost:8088/webapp/user/list
	
	http://localhost:8088/webapp/user/8
	
	http://localhost:8088/webapp/login
