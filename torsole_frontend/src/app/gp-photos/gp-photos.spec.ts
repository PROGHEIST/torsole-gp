import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GpPhotos } from './gp-photos';

describe('GpPhotos', () => {
  let component: GpPhotos;
  let fixture: ComponentFixture<GpPhotos>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [GpPhotos]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GpPhotos);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
