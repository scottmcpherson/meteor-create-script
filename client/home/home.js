Session.setDefault('clickCount', 0);

Template.home.events({
   'click input': function() {
      Session.set('clickCount', Session.get('clickCount') + 1);
   }
});

Template.home.clickCount = function() {
   return Session.get('clickCount');
}