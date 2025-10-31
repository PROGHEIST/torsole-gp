import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { Api } from '../../api';

@Component({
  selector: 'app-gp-bodies',
  standalone: false,
  templateUrl: './gp-bodies.html',
  styleUrl: './gp-bodies.css'
})
export class GpBodies implements OnInit {

  gpBodiesData: any[] = [];
  isLoading: boolean = true;

  constructor(private api: Api, private cdr: ChangeDetectorRef) {}

  ngOnInit(): void {
    this.api.getGPBodiesData().subscribe(
      (data) => {
        this.gpBodiesData = data;
        this.isLoading = false;
        this.cdr.detectChanges();
      },
      (error) => {
        console.error('Error fetching GP Bodies data:', error);
        this.isLoading = false;
        this.cdr.detectChanges();
      }
    );
}
}