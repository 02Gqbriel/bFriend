import { Component } from '@angular/core';
import axios, { AxiosResponse } from 'axios';
import {Injectable} from "@angular/core";

@Injectable({
  providedIn: 'root'
})

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  onClickSubmit(data: any ){
    const formData = new FormData();
    formData.append("username",data.username);
    formData.append("password",data.password);

    console.log(data);
    axios
      .post('http://localhost:5000/auth/login', formData)
      .then((response: AxiosResponse) => {
        console.log("your logged In")
    })
      .catch((error: any) => {
        console.log(error)
      })
    }
}
