import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { DatePipe, CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Api } from '../api';
import { forkJoin } from 'rxjs';

@Component({
  selector: 'app-government-gr',
  templateUrl: './government-gr.html',
  styleUrls: ['./government-gr.css'],
  imports: [DatePipe, FormsModule, CommonModule]
})
export class GovernmentGr implements OnInit {
  government_grs: any[] = [];
  filtered_grs: any[] = [];
  loading: boolean = true;
  selectedDepartment: string = '';
  selectedCategory: string = '';
  searchQuery: string = '';
  departments: string[] = [];
  categories: string[] = [];
  departmentNames: { [key: string]: string } = {};

  constructor(private api: Api, private cdr: ChangeDetectorRef) {}

  ngOnInit(): void {
    forkJoin({
      grs: this.api.getGovernmentGrData(),
      departments: this.api.getGRDepartmentData()
    }).subscribe(
      ({ grs, departments }: { grs: any[], departments: any[] }) => {
        this.government_grs = grs;
        this.filtered_grs = grs;
        // Set departments from API
        this.departments = departments.map((dept: any) => String(dept.id));
        // Create department names mapping
        this.departmentNames = departments.reduce((acc: { [key: string]: string }, dept: any) => {
          acc[String(dept.id)] = dept.name;
          return acc;
        }, {} as { [key: string]: string });
        this.categories = [...new Set(grs.map((gr: any) => gr.category))];
        this.loading = false;
        this.cdr.detectChanges();
      },
      (error: any) => {
        console.error('Error fetching data:', error);
        this.loading = false;
        this.cdr.detectChanges();
      }
    );
  }

  filterGrs(): void {
    this.filtered_grs = this.government_grs.filter(gr =>
      (this.selectedDepartment ? gr.department == this.selectedDepartment : true) &&
      (this.selectedCategory ? gr.category === this.selectedCategory : true) &&
      (this.searchQuery ? (gr.title.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
                           gr.description.toLowerCase().includes(this.searchQuery.toLowerCase())) : true)
    );
  }
}
