import React,{useState} from "react"
import {Accordion,Card} from "react-bootstrap";
import './App.css';
function RenderAccordian({item,index}){

    
    return (<Accordion >
    <Card key={index}>
      <Accordion.Toggle as={Card.Header} eventKey={item.id}>
        {item.abbreviation}
      </Accordion.Toggle>
      <Accordion.Collapse eventKey={item.id}>
        <Card.Body>{item.city}</Card.Body>
      </Accordion.Collapse>
    </Card>
  </Accordion>)

}
// RenderAccordian.defaultProps={
//     item:"15454654",
//     content:"hello i am accordian",
// };
export default RenderAccordian;
