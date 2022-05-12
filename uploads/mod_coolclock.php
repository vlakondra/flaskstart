<?php

/**
 * @version SVN: $Id$
 * @package    CoolClock
 * @subpackage Base
 * @author     Michael Richey {@link http://www.richeyweb.com}
 * @author     Created on 20-Feb-2010
 */
//-- No direct access
defined('_JEXEC') or die('=;)');
JHtml::_('behavior.framework');
$doc = JFactory::getDocument();
foreach (array('excanvas.js', 'coolclock.js', 'moreskins.js') as $script)
    $doc->addScript(JURI::root(true) . DIRECTORY_SEPARATOR . 'media' . DIRECTORY_SEPARATOR . 'mod_coolclock' . DIRECTORY_SEPARATOR . 'assets' . DIRECTORY_SEPARATOR . 'js' . DIRECTORY_SEPARATOR . $script);
$declaration = array();
if ($params->get('skin') == 'custom') {
    $declaration[] = 'CoolClock.config.skins[\'custom' . $module->id . '\'] = {';
    $declaration[] = '  outerBorder: { lineWidth: ' . $params->get('outerBorder-lineWidth') . ', radius:' . $params->get('outerBorder-radius') . ', color: "' . $params->get('outerBorder-color') . '", alpha: ' . $params->get('outerBorder-alpha') . ' },';
    $declaration[] = '  smallIndicator: { lineWidth: ' . $params->get('smallIndicator-lineWidth') . ', startAt: ' . $params->get('smallIndicator-startAt') . ', endAt: ' . $params->get('smallIndicator-endAt') . ', color: "' . $params->get('smallIndicator-color') . '", alpha: ' . $params->get('smallIndicator-alpha') . ' },';
    $declaration[] = '  largeIndicator: { lineWidth: ' . $params->get('largeIndicator-lineWidth') . ', startAt: ' . $params->get('largeIndicator-startAt') . ', endAt: ' . $params->get('largeIndicator-endAt') . ', color: "' . $params->get('largeIndicator-color') . '", alpha: ' . $params->get('largeIndicator-alpha') . ' },';
    $declaration[] = '  hourHand: { lineWidth: ' . $params->get('hourHand-lineWidth') . ', startAt: ' . $params->get('hourHand-startAt') . ', endAt: ' . $params->get('hourHand-endAt') . ', color: "' . $params->get('hourHand-color') . '", alpha: ' . $params->get('hourHand-alpha') . ' },';
    $declaration[] = '  minuteHand: { lineWidth: ' . $params->get('minuteHand-lineWidth') . ', startAt: ' . $params->get('minuteHand-startAt') . ', endAt: ' . $params->get('minuteHand-endAt') . ', color: "' . $params->get('minuteHand-color') . '", alpha: ' . $params->get('minuteHand-alpha') . ' },';
    $declaration[] = '  secondHand: { lineWidth: ' . $params->get('secondHand-lineWidth') . ', startAt: ' . $params->get('secondHand-startAt') . ', endAt: ' . $params->get('secondHand-endAt') . ', color: "' . $params->get('secondHand-color') . '", alpha: ' . $params->get('secondHand-alpha') . ' },';
    $declaration[] = '  secondDecoration: { lineWidth: ' . $params->get('secondDecoration-lineWidth') . ', startAt: ' . $params->get('secondDecoration-startAt') . ', radius: ' . $params->get('secondDecoration-radius') . ', fillColor: "' . $params->get('secondDecoration-fillColor') . '", color: "' . $params->get('secondDecoration-color') . '", alpha: ' . $params->get('secondDecoration-alpha') . ' }';
    $declaration[] = '};';
}
$declaration[] = 'Date.prototype.getUTCTime = function(){ ';
    $declaration[] = "\treturn new Date(";
        $declaration[] = "\t\tthis.getUTCFullYear(),";
        $declaration[] = "\t\tthis.getUTCMonth(),";
        $declaration[] = "\t\tthis.getUTCDate(),";
        $declaration[] = "\t\tthis.getUTCHours(),";
        $declaration[] = "\t\tthis.getUTCMinutes(), ";
        $declaration[] = "\t\tthis.getUTCSeconds()";
    $declaration[] = "\t).getTime(); ";
$declaration[] = '};';
$daystart = $params->get('daytimestart', 6);
$dayend = $params->get('daytimeend', 18);
$offset = ((float) trim($params->get('offset', 0))) * 3600000;
$declaration[] = "\nwindow.setInterval(function(){";
    $declaration[] = "\tvar time = new Date().getUTCTime();";
    $declaration[] = "\tvar offsettime = new Date(time + " . $offset . ");";
    $declaration[] = "\tvar hour = offsettime.getHours();";
    $declaration[] = "\tvar aclass = (hour >= " . $daystart . " && hour < " . $dayend . ")?'day':'night';";
    $declaration[] = "\tvar rclass = (aclass==='night')?'day':'night';";
    $declaration[] = "\tvar el = document.getElementById('clock" . $module->id . "');";
    $declaration[] = "\tvar elclasses = el.className.split(' ');";
    $declaration[] = "\tif(i = elclasses.indexOf(rclass)) delete elclasses[i];";
    $declaration[] = "\tif(elclasses.indexOf(aclass) == -1) elclasses.push(aclass);";
    $declaration[] = "\tel.className = elclasses.join(' ');";
$declaration[] = '},1000);';
if (count($declaration) > 0)
    $doc->addScriptDeclaration("\n" . implode("\n", $declaration) . "\n");
//-- Include the template for display
require JModuleHelper::getLayoutPath('mod_coolclock');
