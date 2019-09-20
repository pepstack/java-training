package com.pepstack.webapp.controller;

import java.util.List;
import java.util.ArrayList;

import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;

import com.pepstack.webapp.model.User;

// 一定是 Controller, 不能是 RestController
@Controller
@RequestMapping("/user")
public class UserController {
    
    @RequestMapping("/{id}") 
    public String  getUser(@PathVariable int id, Model model) {
		
		User dto = new User();

		dto.setId((long) id);
		dto.setUsername("pepstack-"+id);
		dto.setAddress("Shanghai, China");
		dto.setAge(20 + id);
        
        model.addAttribute("user", dto);

        return "/user/detail";
    }


    @RequestMapping("/list")
    public String  listUser(Model model) {
        List<User> userList = new ArrayList<User>();

        for (int i = 0; i < 9; i++) {
			User dto = new User();

			dto.setId((long) i);
			dto.setUsername("pepstack-" + i);
			dto.setAddress("Shanghai, China");
			dto.setAge(20 + i);
			
            userList.add(dto);
        }

        model.addAttribute("users", userList);

        return "/user/list";
    }


	@RequestMapping("/login")
    public String  login(Model model) {
        // model.addAttribute("users", userList);

        return "/login";
    }
}
