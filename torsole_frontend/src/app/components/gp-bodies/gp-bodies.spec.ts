import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GpBodies } from './gp-bodies';

describe('GpBodies', () => {
  let component: GpBodies;
  let fixture: ComponentFixture<GpBodies>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [GpBodies]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GpBodies);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
