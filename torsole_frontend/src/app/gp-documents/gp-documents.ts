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

  constructor(private api: Api, private cdr: ChangeDetectorRef){}

  ngOnInit(): void {
    this.api.getGPDocumentsData().subscribe(
      (data) => {
        this.gpDocuments = data;
        this.cdr.detectChanges();
      },
      (error) => {
        console.log("failed to fetch the documents", error)
      }
    )
  }
}
