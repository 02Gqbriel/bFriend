import {Component, OnInit} from '@angular/core';
import axios, {AxiosResponse} from "axios";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit{
  userData: any[] = [];
  i: number = 0;

  constructor() {
    this.renderHomepage()
  }
  renderHomepage () {
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
