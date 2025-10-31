import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Home } from './home/home';
import { Mission } from './mission/mission';
import { GovernmentGr } from './government-gr/government-gr';
import { GpDocuments } from './gp-documents/gp-documents';
import { GpPhotos } from './gp-photos/gp-photos';
import { GpEmployee } from './gp-employee/gp-employee';


const routes: Routes = [
  {path: '', component: Home},
  {path: 'objectives', component: Mission},
  {path: 'government-grs', component: GovernmentGr},
  {path: 'gp-documents', component: GpDocuments},
  {path: 'photo-gallery', component: GpPhotos},
  {path: 'gp-bodies', component: GpEmployee},
  {path: '**', redirectTo: ''}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
