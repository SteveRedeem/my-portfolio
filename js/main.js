import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work';

const myWork = [
  {
    'title': "Work example",
    'image': {
      'desc': "code example project",
      'src': "images/example1.png",
      'comment': ""
    }
  },
  {
    'title': "Boilerplate",
    'image': {
      'desc': "Serverless Portfolio",
      'src': "images/example2.png",
      'comment': ""
    }
  },
  {
    'title': "",
    'image': {
      'desc': "example screen shot",
      'src': "images/example3.png",
      'comment': `"Bengal cat" by rob shabis licensed under CC BY 2.0
           https://www.flickr.com/photos/37287295@N00/2540855181"`
    }
  }
]
ReactDOM.render(<ExampleWork work={myWork}/>, document.getElementById('example-work'));
