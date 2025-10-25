import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { Api } from '../api';

@Component({
  selector: 'app-gp-photos',
  standalone: false,
  templateUrl: './gp-photos.html',
  styleUrl: './gp-photos.css'
})
export class GpPhotos implements OnInit{

  gpPhotos: any[] = [];
  selectedPhoto: any = null;

  constructor(private api: Api, private cdr: ChangeDetectorRef){}

  ngOnInit(): void {
    this.api.getPhotoGalleryData().subscribe(
      (data) => {
        this.gpPhotos = data;
        this.cdr.detectChanges();
      },
      (error) => {
        console.log("failed to fetch photos", error)
      }
    )
  }

  openFullscreen(photo: any): void {
    this.selectedPhoto = photo;
  }

  closeFullscreen(): void {
    this.selectedPhoto = null;
  }

  downloadPhoto(photo: any): void {
    const link = document.createElement('a');
    link.href = photo.image;
    link.download = photo.title || 'photo.jpg';
    link.click();
  }

}
