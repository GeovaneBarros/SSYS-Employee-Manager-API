import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EmplooyeListComponent } from './compoments/emplooye-list/emplooye-list.component';

const routes: Routes = [
  {path:'emplooyes', component:EmplooyeListComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
