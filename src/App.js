import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import RenderAccordian from "./RenderAccordian"
function App(props) {

  return (
    <div className="App">
      {props.arr.map((item,index)=><RenderAccordian item={item} index={index}/>)}
    </div>
  );
}
App.defaultProps={arr:[
  {
  "id":1,
  "abbreviation":"ATL",
  "city":"Atlanta"
  
  },
  {
  "id":2,
  "abbreviation":"BOS",
  "city":"Boston"
  },
 {
  "id":3,
  "abbreviation":"BKN",
  "city":"Brooklyn"
 
  },
{
  "id":4,
  "abbreviation":"CHA",
  "city":"Charlotte"
  },
{
  "id":5,
  "abbreviation":"CHI",
  "city":"Chicago"
  },
{
  "id":6,
  "abbreviation":"CLE",
  "city":"Cleveland",
  },
 {
  "id":7,
  "abbreviation":"DAL",
  "city":"Dallas",
  },
{
  "id":8,
  "abbreviation":"DEN",
  "city":"Denver",
  },
  {
  "id":9,
  "abbreviation":"DET",
  "city":"Detroit",
  },
{
  "id":10,
  "abbreviation":"GSW",
  "city":"Golden State"
  },
{
  "id":11,
  "abbreviation":"HOU",
  "city":"Houston",

  }]}
export default App;
