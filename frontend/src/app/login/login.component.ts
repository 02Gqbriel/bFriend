import { Component } from '@angular/core';
import axios, { AxiosResponse } from 'axios';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  onClicksubmit(data: any ){
    console.log(data);
    const inputs = [data.username, data.password]
    axios
      .post('http://localhost:5000/auth/login', inputs)
      .then((response: AxiosResponse) => {
        console.log("your logged In")
    })
      .catch((error: any) => {
        console.log(error)
      })
    }
}
