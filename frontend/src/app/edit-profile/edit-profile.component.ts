import { Component, OnInit } from '@angular/core';
import axios, { AxiosResponse } from "axios";

@Component({
  selector: 'app-edit-profile',
  templateUrl: './edit-profile.component.html',
  styleUrls: ['./edit-profile.component.css']
})
export class EditProfileComponent implements OnInit {

  userData: any[] = [];

  constructor() {
    this.get_user_session();
  }

  ngOnInit() {
    // Other initialization logic
  }

  get_user_session() {


    const formData = new FormData();
    formData.append("userID", '1');

    axios
      .post("http://localhost:5000/user_actions/select-user", formData)
      .then((response: AxiosResponse) => {
        console.log("user data has been received");
        console.log(response.data);
        this.userData = response.data;
      })
      .catch((error: any) => {
        console.log(error);
      });
  }

  set_user_firstname(name: string) {
    //user_firstname = name;
  }

  get_user_firstname() {
    //return user_firstname;
  }

    edit_profile_onClick(data: any ){

    if (data.password == data.password_confirm) {

      for (let i = 0; i < 5000; i++){
        const response_status = document.getElementById("success");
        const p = document.createElement("p");
        p.textContent = "All changes have been saved";
        response_status?.appendChild(p);
      }


      const formData = new FormData();

      formData.append("firstname", data.firstname);
      formData.append("lastname", data.lastname);
      formData.append("age", data.age);
      formData.append("username", data.username);
      formData.append("email", data.email);
      formData.append("password", data.password);
      formData.append("hobby", data.hobbies)

      console.log(formData);
      axios
        .post('http://localhost:5000/user_actions/edit-user', formData)
        .then((response: AxiosResponse) => {
          console.log("user data has been submitted")
        })
        .catch((error: any) => {
          console.log(error)
        })
    }
    else{
      console.log("password does not match")
      const response_status = document.getElementById("success");
      const p = document.createElement("p");
      p.textContent = "password does not match";
      response_status?.appendChild(p);
    }

  }
}
