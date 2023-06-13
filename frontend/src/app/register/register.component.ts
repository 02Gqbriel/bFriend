import { Component } from '@angular/core';
import axios, {AxiosResponse} from "axios";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})

export class RegisterComponent {
  onClickSubmit(data: any ){
    const formData = new FormData();
    formData.append("username",data.username);
    formData.append("password",data.password);
    formData.append("firstname",data.firstname);
    formData.append("lastname",data.lastname);
    console.log(formData)
    axios
      .post('http://localhost:5000/auth/register', formData)
      .then((response: AxiosResponse) => {
        console.log("registration succesfully")
    })
      .catch((error: any) => {
        console.log(error)
      })
    }
}
