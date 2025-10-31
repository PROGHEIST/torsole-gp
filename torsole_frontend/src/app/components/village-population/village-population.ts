import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { Api } from '../../api';

@Component({
  selector: 'app-village-population',
  standalone: false,
  templateUrl: './village-population.html',
  styleUrl: './village-population.css'
})
export class VillagePopulation implements OnInit {

  populationData: any[] = [];
  maxPopulation: number = 0;
  totalPopulation: number = 0;
  averagePopulation: number = 0;


  constructor(private cdr: ChangeDetectorRef, private api: Api) {}

  ngOnInit() {
    this.api.getVillagePopulationData().subscribe({
      next: (data) => {
        this.populationData = data;
        this.calculateStats();
        this.cdr.detectChanges();
      },
      error: (err) => {
        console.error('Error fetching village population data:', err);
        // Optionally set default data or show error message
      }
    });
  }



  calculateStats() {
    if (this.populationData.length > 0) {
      this.maxPopulation = Math.max(...this.populationData.map(item => item.population || 0));
      this.totalPopulation = this.populationData.reduce((sum, item) => sum + (item.population || 0), 0);
      this.averagePopulation = Math.round(this.totalPopulation / this.populationData.length);
    }
  }



}
