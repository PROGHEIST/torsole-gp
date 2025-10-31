import { NgModule, provideBrowserGlobalErrorListeners, provideZonelessChangeDetection } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing-module';
import { App } from './app';
import { Navbar } from './components/navbar/navbar';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule, DatePipe } from '@angular/common';
import { Footer } from './components/footer/footer';
import { Home } from './home/home';
import { Slideshow } from './components/slideshow/slideshow';
import { Mission } from './mission/mission';
import { OurMission } from './components/our-mission/our-mission';
import { ImpLinks } from './components/imp-links/imp-links';
import { MapLocation } from './components/map-location/map-location';
import { GovernmentGr } from './government-gr/government-gr';
import { FormsModule } from '@angular/forms';
import { GpDocuments } from './gp-documents/gp-documents';
import { GpPhotos } from './gp-photos/gp-photos';
import { GpBodies } from './components/gp-bodies/gp-bodies';
import { GpEmployee } from './gp-employee/gp-employee';
import { MahaOfficers } from './components/maha-officers/maha-officers';
import { VillagePopulation } from './components/village-population/village-population';

@NgModule({
  declarations: [
    App,
    Navbar,
    Footer,
    Home,
    Slideshow,
    GpBodies,
    Mission,
    OurMission,
    ImpLinks,
    MapLocation,
    GpDocuments,
    GpPhotos,
    GpEmployee,
    MahaOfficers,
    VillagePopulation
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    CommonModule,
    FormsModule,
    GovernmentGr
  ],
  providers: [
    provideBrowserGlobalErrorListeners(),
    provideZonelessChangeDetection(),
    DatePipe
  ],
  bootstrap: [App]
})
export class AppModule { }
