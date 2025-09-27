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

@NgModule({
  declarations: [
    App,
    Navbar,
    Footer,
    Home,
    Slideshow
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
