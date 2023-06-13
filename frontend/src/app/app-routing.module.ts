import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import {ProfileComponent} from "./profile/profile.component";
import {EditProfileComponent} from "./edit-profile/edit-profile.component";
import {AddMediaComponent} from "./add-media/add-media.component";
import {SettingsComponent} from "./settings/settings.component";

const routes: Routes = [
    { path: '', title: 'Home', component: HomeComponent },
    { path: 'login', title: 'Login', component: LoginComponent },
    { path: 'register', title: 'Register', component: RegisterComponent },
    { path: 'profile', title: 'Profile', component: ProfileComponent },
    { path: 'profile/edit_profile', title: 'Edit profile', component: EditProfileComponent },
    { path: 'profile/add_media', title: 'Add media', component: AddMediaComponent },
    { path: 'profile/settings', title: 'Settings', component: SettingsComponent },

    // otherwise redirect to home
    { path: '**', redirectTo: '' }
];

export const AppRoutingModule = RouterModule.forRoot(routes);
