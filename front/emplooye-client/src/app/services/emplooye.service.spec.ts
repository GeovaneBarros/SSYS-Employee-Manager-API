import { TestBed } from '@angular/core/testing';

import { EmplooyeService } from './emplooye.service';

describe('EmplooyeService', () => {
  let service: EmplooyeService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EmplooyeService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
