import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GpEmployee } from './gp-employee';

describe('GpEmployee', () => {
  let component: GpEmployee;
  let fixture: ComponentFixture<GpEmployee>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [GpEmployee]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GpEmployee);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
