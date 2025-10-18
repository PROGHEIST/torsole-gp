import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GovernmentGr } from './government-gr';

describe('GovernmentGr', () => {
  let component: GovernmentGr;
  let fixture: ComponentFixture<GovernmentGr>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [GovernmentGr]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GovernmentGr);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
