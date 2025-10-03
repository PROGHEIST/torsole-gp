import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ImpLinks } from './imp-links';

describe('ImpLinks', () => {
  let component: ImpLinks;
  let fixture: ComponentFixture<ImpLinks>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ImpLinks]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ImpLinks);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
