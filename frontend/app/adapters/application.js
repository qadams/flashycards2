/* import DS from 'ember-data';
import { computed } from '@ember/object';
export default DS.RESTAdapter.extend({
  host: computed(function(){
    return 'http://localhost:8000';
  }),
  namespace: 'api'
});

*/

import DS from 'ember-data';

export default DS.JSONAPIAdapter.extend({
  namespace: 'api'
});
