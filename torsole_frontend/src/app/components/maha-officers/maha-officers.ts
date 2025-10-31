import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { of } from 'rxjs';
import { Api } from '../../api';

@Component({
  selector: 'app-maha-officers',
  standalone: false,
  templateUrl: './maha-officers.html',
  styleUrl: './maha-officers.css'
})
export class MahaOfficers implements OnInit {

  officersData: any[] = [];

  constructor(private api: Api, private cdr: ChangeDetectorRef) {}

  ngOnInit(): void {
    this.api.getMahaOfficersData().subscribe((data) => {
      this.officersData = data;
      this.cdr.detectChanges();
    },
    (error) => {
      console.error('Error fetching Maharashtra officers data:', error);
    });
  }

}
