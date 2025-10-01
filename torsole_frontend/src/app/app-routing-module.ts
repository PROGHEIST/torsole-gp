import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Home } from './home/home';
import { Mission } from './mission/mission';

const routes: Routes = [
  {path: '', component: Home},
  {path: 'objectives', component: Mission}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
