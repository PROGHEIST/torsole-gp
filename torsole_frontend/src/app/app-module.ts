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

@NgModule({
  declarations: [
    App,
    Navbar,
    Footer,
    Home,
    Slideshow,
    GpBodies,
    Mission,
    OurMission
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    CommonModule
  ],
  providers: [
    provideBrowserGlobalErrorListeners(),
    provideZonelessChangeDetection()
  ],
  bootstrap: [App]
})
export class AppModule { }
