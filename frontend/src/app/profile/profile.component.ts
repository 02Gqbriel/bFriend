import { Component } from '@angular/core';
import axios, {AxiosResponse} from "axios";

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {
  userData: any[] = [];
  i: number = 0;

  constructor() {
    this.renderProfile()
  }
  renderProfile () {
    axios
      .post('http://localhost:5000/user_actions/get-all')
      .then((response: AxiosResponse) => {
        this.userData = response.data
        console.log(this.userData)
    })
      .catch((error: any) => {
        console.log(error)
      })
    }

  ngOnInit(): void {

  }

  btnClick() {
    this.i = this.i + 1;

  }
}
