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
  searchTerm: string = '';
  selectedCategory: string = '';
  categories: string[] = [];

  constructor(private api: Api, private cdr: ChangeDetectorRef){}

  ngOnInit(): void {
    this.api.getPhotoGalleryData().subscribe(
      (data) => {
        this.gpPhotos = data;
        this.categories = Array.from(new Set(data.map((photo: any) => photo.category as string)));
        this.cdr.detectChanges();
      },
      (error) => {
        console.log("failed to fetch photos", error)
      }
    )
  }

  get filteredPhotos(): any[] {
    return this.gpPhotos.filter(photo => {
      const matchesSearch = photo.title.toLowerCase().includes(this.searchTerm.toLowerCase());
      const matchesCategory = this.selectedCategory === '' || photo.category === this.selectedCategory;
      return matchesSearch && matchesCategory;
    });
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

  trackByFn(index: number, item: any): any {
    return item.id || index;
  }

}
