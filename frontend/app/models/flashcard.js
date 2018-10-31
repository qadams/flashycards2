import DS from 'ember-data';

export default DS.Model.extend({
  term: DS.attr(),
  defintion: DS.attr()
});
