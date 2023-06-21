import { Component } from '@angular/core';
import axios, {AxiosResponse} from "axios";

@Component({
  selector: 'app-edit-profile',
  templateUrl: './edit-profile.component.html',
  styleUrls: ['./edit-profile.component.css']
})



export class EditProfileComponent {
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
      formData.append("firstname", data.lastname);
      formData.append("firstname", data.age);
      formData.append("username", data.username);
      formData.append("email", data.email);
      formData.append("password", data.password);
      formData.append("password_confirm", data.password_confirm);

      console.log(formData);
      axios
        .post('http://localhost:5000/auth/update', formData)
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
  get_user_session(){
    axios
      .post("http://localhost:5000/user_actions/select-user", 1)
              .then((response: AxiosResponse) => {
          console.log("user data has been received")
                  //this.set_user_firstname(response.data[0]);
                console.log(response.data)
        })
        .catch((error: any) => {
          console.log(error)
        })
  }

  set_user_firstname(name:string){
      //user_firstname = name;
  }
  get_user_firstname(){
       //return user_firstname;
  }

}
