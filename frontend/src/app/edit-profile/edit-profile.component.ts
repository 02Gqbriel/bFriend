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
      const formData = new FormData();
      formData.append("username", data.username);
      formData.append("password", data.password);
      formData.append("password_confirm", data.password_confirm);

      console.log(formData);
      axios
        .post('http://localhost:5000/update/user', formData)
        .then((response: AxiosResponse) => {
          console.log("user data has been submitted")
        })
        .catch((error: any) => {
          console.log(error)
        })
    }
    else{
      console.log("password does not match")
    }
  }
}
