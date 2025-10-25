import { NgModule, provideBrowserGlobalErrorListeners, provideZonelessChangeDetection } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing-module';
import { App } from './app';
import { Navbar } from './components/navbar/navbar';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { Footer } from './components/footer/footer';
import { Home } from './home/home';
import { Slideshow } from './components/slideshow/slideshow';
import { GpBodies } from './components/gp-bodies/gp-bodies';
import { Mission } from './mission/mission';
import { OurMission } from './components/our-mission/our-mission';
import { ImpLinks } from './components/imp-links/imp-links';
import { MapLocation } from './components/map-location/map-location';
import { GovernmentGr } from './government-gr/government-gr';
import { FormsModule } from '@angular/forms';
import { GpDocuments } from './gp-documents/gp-documents';
import { GpPhotos } from './gp-photos/gp-photos';

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
    GpPhotos
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
    provideZonelessChangeDetection()
  ],
  bootstrap: [App]
})
export class AppModule { }
