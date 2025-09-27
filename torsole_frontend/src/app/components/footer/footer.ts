import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { Api } from '../../api';

@Component({
  selector: 'app-footer',
  standalone: false,
  templateUrl: './footer.html',
  styleUrl: './footer.css'
})
export class Footer implements OnInit {
  appData: any[] = [];

  constructor(private api: Api, private cdr: ChangeDetectorRef) {}

  ngOnInit(): void {
    this.api.getAppData().subscribe(
      (data) => {
        this.appData = data;
        console.log(this.appData);
        this.cdr.detectChanges();
      },
      (err: any) => {
        console.log("data not fetched!", err);
      }
    );
  }
}
