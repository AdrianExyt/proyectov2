import { NgModule } from '@angular/core';
import { RouterModule, Routes, ActivatedRoute, ParamMap } from '@angular/router';
import { SearchComponent } from './search/search.component';
import { FormComponent } from './form/form.component';
import { EditComponent } from './edit/edit.component';

const routes: Routes = [
  { path: 'form-component', component: FormComponent},
  { path: 'search-component', component: SearchComponent},
  { path: 'edit-component/:id', component: EditComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
