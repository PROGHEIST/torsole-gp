import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Home } from './home/home';
import { Mission } from './mission/mission';
import { GovernmentGr } from './government-gr/government-gr';

const routes: Routes = [
  {path: '', component: Home},
  {path: 'objectives', component: Mission},
  {path: 'government-grs', component: GovernmentGr}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
