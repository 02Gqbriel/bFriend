import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import {ProfileComponent} from "./profile/profile.component";

const routes: Routes = [
    { path: '', title: 'Home', component: HomeComponent },
    { path: 'login', title: 'Login', component: LoginComponent },
    { path: 'register', title: 'Register', component: RegisterComponent },
    { path: 'profile', title: 'Profile', component: ProfileComponent },

    // otherwise redirect to home
    { path: '**', redirectTo: '' }
];

export const AppRoutingModule = RouterModule.forRoot(routes);
