import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { Api } from '../../api';

@Component({
  selector: 'app-our-mission',
  standalone: false,
  templateUrl: './our-mission.html',
  styleUrl: './our-mission.css'
})
export class OurMission implements OnInit{

  missions: any[] = [];
  loading: boolean = true;

  constructor (private api: Api, private cdr: ChangeDetectorRef) {}

  ngOnInit(): void {
    this.api.getMissionsData().subscribe(
      (data) => {
        this.missions = data;
        this.loading = false;
        this.cdr.detectChanges();
      },
      (error) => {
        console.error("failed to fetch", error);
        this.loading = false;
      }
    )
  }

}
