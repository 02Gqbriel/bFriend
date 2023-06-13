import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddMediaComponent } from './add-media.component';

describe('AddMediaComponent', () => {
  let component: AddMediaComponent;
  let fixture: ComponentFixture<AddMediaComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AddMediaComponent]
    });
    fixture = TestBed.createComponent(AddMediaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
