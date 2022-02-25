import { Component, OnInit } from '@angular/core';
import { EmplooyeService } from 'src/app/services/emplooye.service';

@Component({
  selector: 'app-emplooye-list',
  templateUrl: './emplooye-list.component.html',
  styleUrls: ['./emplooye-list.component.css']
})
export class EmplooyeListComponent implements OnInit {

  constructor(private emplooyeService: EmplooyeService) { }
  
  emplooyes: any;

  ngOnInit(): void {
    this.getAll();
  }
  getAll(): void{
    this.emplooyeService.getAll().subscribe(
      emplooyes => {
        this.emplooyes = emplooyes;
        console.log(emplooyes)
      },
      error => {
        console.log(error);
      }
    );
  }
}
