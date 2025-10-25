import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { Api } from '../api';

@Component({
  selector: 'app-gp-documents',
  standalone: false,
  templateUrl: './gp-documents.html',
  styleUrl: './gp-documents.css'
})
export class GpDocuments implements OnInit{

  gpDocuments: any[] = [];
  filteredDocuments: any[] = [];
  categories: string[] = [];
  selectedCategory: string = '';

  constructor(private api: Api, private cdr: ChangeDetectorRef){}

  ngOnInit(): void {
    this.api.getGPDocumentsData().subscribe(
      (data: any[]) => {
        this.gpDocuments = data;
        this.filteredDocuments = data;
        this.categories = [...new Set(data.map((item: any) => item.category))];
        console.log(this.categories)
        this.cdr.detectChanges();
      },
      (error) => {
        console.log("failed to fetch the documents", error)
      }
    );
  }

  filterByCategory(category: string): void {
    this.selectedCategory = category;
    if (category) {
      this.filteredDocuments = this.gpDocuments.filter(doc => doc.category === category);
    } else {
      this.filteredDocuments = this.gpDocuments;
    }
    this.cdr.detectChanges();
  }
}
