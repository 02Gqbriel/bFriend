import { Component } from '@angular/core';
import axios, {AxiosResponse} from "axios";

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent {
  deleteAccount(){
    const formData = new FormData()
    formData.append("userID", "1");
    axios
      .post('http://localhost:5000/user_actions/delete-user', formData)
      .then((response: AxiosResponse) => {
        console.log("your logged In")
        console.log(response)
    })
      .catch((error: any) => {
        console.log(error)
      })
    }
}
