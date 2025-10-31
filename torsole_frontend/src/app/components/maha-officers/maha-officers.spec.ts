import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MahaOfficers } from './maha-officers';

describe('MahaOfficers', () => {
  let component: MahaOfficers;
  let fixture: ComponentFixture<MahaOfficers>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [MahaOfficers]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MahaOfficers);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
