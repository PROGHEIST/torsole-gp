import { Component, OnInit, OnDestroy, ChangeDetectorRef, NgZone, HostListener } from '@angular/core';
import { Api } from '../../api';


@Component({
  selector: 'app-slideshow',
  standalone: false,
  templateUrl: './slideshow.html',
  styleUrl: './slideshow.css'
})
export class Slideshow implements OnInit, OnDestroy{

  images: any[] = []
  currentIndex: number = 0;
  private interval: any;
  private touchStartX: number = 0;

  constructor(public api: Api, private cdr: ChangeDetectorRef, private ngZone: NgZone) {}

  ngOnInit(): void {
    this.api.getCarosoulData().subscribe(
      (data) => {
        this.images = data;
        console.log(this.images);
        this.cdr.detectChanges();
        if (this.images.length > 0) {
          this.interval = setInterval(() => this.ngZone.run(() => this.next()), 5000);
        }
      },
      (err) => {
        console.log("error fetching images", err);
      });
  }

  ngOnDestroy(): void {
    if (this.interval) {
      clearInterval(this.interval);
    }
  }

  @HostListener('touchstart', ['$event'])
  onTouchStart(event: TouchEvent): void {
    this.touchStartX = event.touches[0].clientX;
  }

  @HostListener('touchend', ['$event'])
  onTouchEnd(event: TouchEvent): void {
    const touchEndX = event.changedTouches[0].clientX;
    const deltaX = this.touchStartX - touchEndX;
    if (Math.abs(deltaX) > 50) {
      if (deltaX > 0) {
        this.next();
      } else {
        this.prev();
      }
    }
  }

  next(): void {
    if (this.images.length === 0) return;
    this.currentIndex = (this.currentIndex + 1) % this.images.length;
    this.cdr.detectChanges();
  }

  prev(): void {
    if (this.images.length === 0) return;
    this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
    this.cdr.detectChanges();
  }
}
