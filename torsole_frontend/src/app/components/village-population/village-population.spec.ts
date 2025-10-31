import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VillagePopulation } from './village-population';

describe('VillagePopulation', () => {
  let component: VillagePopulation;
  let fixture: ComponentFixture<VillagePopulation>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [VillagePopulation]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VillagePopulation);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
