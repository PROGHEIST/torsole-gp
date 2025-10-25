import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GpDocuments } from './gp-documents';

describe('GpDocuments', () => {
  let component: GpDocuments;
  let fixture: ComponentFixture<GpDocuments>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [GpDocuments]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GpDocuments);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
