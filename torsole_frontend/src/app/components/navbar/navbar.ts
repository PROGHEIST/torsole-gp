import { Component, OnInit, ChangeDetectorRef, Inject } from '@angular/core';
import { DOCUMENT } from '@angular/common';
import { Api } from '../../api';


@Component({
  selector: 'app-navbar',
  standalone: false,
  templateUrl: './navbar.html',
  styleUrl: './navbar.css'
})
export class Navbar implements OnInit {
  isMenuOpen = false;
  appData: any[] = [];
  isAboutOpen = false;
  isCitizenOpen = false;
  isRTIOpen = false;

  constructor(private api: Api, private cdr: ChangeDetectorRef, @Inject(DOCUMENT) private document: Document) {}

  ngOnInit(): void {
    this.api.getAppData().subscribe(
      (data) => {
        this.appData = data;
        console.log(this.appData);
        this.cdr.detectChanges();
    },
      (err: any) => {
        console.log("data not fetched!", err);
      })
  }

  toggleMenu() {
    this.isMenuOpen = !this.isMenuOpen;
  }

  toggleAbout() {
    this.isAboutOpen = !this.isAboutOpen;
    this.isCitizenOpen = false;
    this.isRTIOpen = false;

    if (this.isAboutOpen && window.innerWidth >= 768) {
      this.document.body.classList.add('overflow-x-hidden');
    } else {
      this.document.body.classList.remove('overflow-x-hidden');
    }
  }

  toggleCitizen() {
    this.isCitizenOpen = !this.isCitizenOpen;
    this.isAboutOpen = false;
    this.isRTIOpen = false;
  }

  toggleRTI() {
    this.isRTIOpen = !this.isRTIOpen;
    this.isAboutOpen = false;
    this.isCitizenOpen = false;
  }
}
