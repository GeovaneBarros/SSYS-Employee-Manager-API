import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EmplooyeListComponent } from './emplooye-list.component';

describe('EmplooyeListComponent', () => {
  let component: EmplooyeListComponent;
  let fixture: ComponentFixture<EmplooyeListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EmplooyeListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EmplooyeListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
