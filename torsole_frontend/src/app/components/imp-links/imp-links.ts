import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { Api } from '../../api';

@Component({
  selector: 'app-imp-links',
  standalone: false,
  templateUrl: './imp-links.html',
  styleUrl: './imp-links.css'
})
export class ImpLinks implements OnInit{
  links: any[] = [];

  constructor(private api: Api, private cdr: ChangeDetectorRef) {}

  ngOnInit(): void {
    this.api.getImpLinksData().subscribe(
      (data) => {
        this.links = data;
        this.cdr.detectChanges();
      },
      (error) => {
        console.error("failed to fetch links", error);
      }
    )
  }
}
